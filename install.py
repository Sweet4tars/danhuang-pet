#!/usr/bin/env python3
"""Install the bundled Danhuang v2 pet using only the Python standard library."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import uuid


PET_ID = "danhuang"
PET_FILES = ("pet.json", "spritesheet.webp")
ROOT = Path(__file__).resolve().parent


def sha256(path):
    with path.open("rb") as handle:
        digest = hashlib.sha256()
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_package():
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("petId") != PET_ID or manifest.get("spriteVersionNumber") != 2:
        raise ValueError("安装清单中的宠物身份或格式不符。")
    expected_paths = {PET_ID + "/" + name for name in PET_FILES}
    if set(manifest.get("files", {})) != expected_paths:
        raise ValueError("安装清单必须恰好包含两个宠物文件。")
    for relative in sorted(expected_paths):
        source = ROOT / relative
        if source.is_symlink() or not source.is_file():
            raise ValueError("缺少或不支持的安装文件：" + relative)
        expected = manifest["files"][relative]
        if source.stat().st_size != expected["size"] or sha256(source) != expected["sha256"]:
            raise ValueError("文件校验失败：" + relative + "，请重新下载。")
    pet = json.loads((ROOT / PET_ID / "pet.json").read_text(encoding="utf-8"))
    if (pet.get("id"), pet.get("spriteVersionNumber"), pet.get("spritesheetPath")) != (
        PET_ID, 2, "spritesheet.webp"
    ):
        raise ValueError("pet.json 中的身份、版本或图集路径不符。")
    return manifest


def install(codex_home, manifest):
    pets = codex_home / "pets"
    target = pets / PET_ID
    if target.is_symlink() or (target.exists() and not target.is_dir()):
        raise ValueError("安装位置不是普通目录，请先检查：" + str(target))
    if target.is_dir() and all(
        (target / name).is_file()
        and not (target / name).is_symlink()
        and sha256(target / name) == manifest["files"][PET_ID + "/" + name]["sha256"]
        for name in PET_FILES
    ):
        print("已是本版蛋黄，无需重复安装：" + str(target))
        return

    pets.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=".danhuang-install-", dir=str(pets)))
    backup = None
    try:
        for name in PET_FILES:
            shutil.copy2(str(ROOT / PET_ID / name), str(stage / name))
            if sha256(stage / name) != manifest["files"][PET_ID + "/" + name]["sha256"]:
                raise ValueError("暂存文件校验失败，未替换原有宠物。")
        if target.exists():
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            backup = codex_home / "pet-backups" / PET_ID / (stamp + "-" + uuid.uuid4().hex[:8])
            backup.parent.mkdir(parents=True, exist_ok=True)
            os.replace(str(target), str(backup))
        try:
            os.replace(str(stage), str(target))
        except OSError:
            if backup is not None and not target.exists():
                os.replace(str(backup), str(target))
            raise
        print("已安装蛋黄 " + manifest["version"] + "：" + str(target))
        if backup is not None:
            print("旧版备份：" + str(backup))
        print("请在桌面客户端的设置 → Pets 中刷新并选择“蛋黄”。")
    finally:
        if stage.exists():
            shutil.rmtree(str(stage))


def main():
    parser = argparse.ArgumentParser(description="校验并安装蛋黄电子宠物；更新前自动备份旧版。")
    parser.add_argument("--verify", action="store_true", help="只校验源文件，不安装")
    parser.add_argument("--codex-home", type=Path, help="指定本机实际使用的 CODEX_HOME")
    args = parser.parse_args()
    try:
        manifest = verify_package()
        print("安装包校验通过：蛋黄 " + manifest["version"] + "，v2 动画图集。")
        if args.verify:
            return 0
        configured = os.environ.get("CODEX_HOME")
        codex_home = args.codex_home or (Path(configured) if configured else Path.home() / ".codex")
        install(codex_home.expanduser().resolve(), manifest)
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("安装未完成：" + str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
