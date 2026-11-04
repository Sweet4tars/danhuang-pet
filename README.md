# 蛋黄 · 毛绒电子宠物

蛋黄是一只保留真实橘金白花色的长毛猫，贪吃、黏人，喜欢歪头、舔爪和甩尾巴。这是可在支持自定义 Pets 的桌面客户端上安装的 v2 动画包。

![蛋黄的三组玩耍动作](previews/toy-actions.gif)

## 用另一台电脑的 Codex 安装

将下面这段话连同仓库地址发给另一台电脑的 Codex：

> 请从 https://github.com/Sweet4tars/danhuang-pet 获取最新版蛋黄，先阅读 README.md 和 install.py，核对 manifest.json 中的文件校验值，然后将它安装到这台电脑的 Pets。使用本机实际的 CODEX_HOME；没有自定义时使用用户目录下的 .codex。已有蛋黄先备份，保留其他宠物，最后告诉我如何刷新并选中蛋黄。

私有仓库需要另一台电脑有相应的 GitHub 访问权限。文件下载到本机后，安装不需要联网。

在下载或克隆的仓库目录中，有 Python 3 时可运行：

```sh
python3 install.py --verify
python3 install.py
```

Windows 通常使用 `py -3 install.py`。如果没有 Python，Codex 也可以校验后手动复制 `danhuang` 文件夹。

默认安装位置是 `<CODEX_HOME>/pets/danhuang/`。没有设置 `CODEX_HOME` 时，macOS 为 `~/.codex/pets/danhuang/`，Windows 为 `%USERPROFILE%\.codex\pets\danhuang\`。使用自定义位置时可运行 `python3 install.py --codex-home "实际路径"`。

安装后在桌面客户端的 **设置 → Pets** 中刷新并选择“蛋黄”；若版本没有刷新按钮，可重新打开客户端。安装工具只负责放置文件，界面是否成功展示仍需在目标电脑确认。不同客户端版本的菜单可能有所不同。

也可下载 [完整安装压缩包](dist/danhuang-pet-v1.1.0.zip)，解压后按上述方式安装。

## 本版动作

保留九类状态和十六个看向方向，将三组玩耍动作放入现有状态：

| 现有状态 | 蛋黄的动作 |
| --- | --- |
| 工作 / running | 用前爪拨动小球 |
| 等待 / waiting | 按住逗猫棒，歪头扑抓羽毛 |
| 完成 / review | 抱住小鱼玩具，后爪轻蹬 |

其他动作和十六个看向方向沿用已经校验的原版。此安装包更新外观动画，不改变客户端的状态触发规则，也不新增喂食或玩具按钮。

## 文件与版本

- `danhuang/pet.json`：名称、简介与 v2 格式声明。
- `danhuang/spritesheet.webp`：1536 × 2288 的透明动画图集。
- `install.py`：仅依赖 Python 标准库的安装工具，支持校验、重复安装检测和旧版备份。
- `manifest.json`、`SHA256SUMS`：版本及文件完整性校验。
- `dist/`：便于跨电脑传输的压缩包。

版本：**1.1.0 · 玩耍版**。图集 SHA-256：

```text
cca3726f5daa1bd07cce4d96238844518c91a5f8094cb1210cd65c0275346c9e
```

自定义宠物通过本仓库在各电脑分别安装；GitHub 仓库更新后，需要在目标电脑重新获取并安装。图集为桌面 v2 格式，使用前需确认客户端支持 v2，不能直接当作其他尺寸格式的素材上传。

动画装配与校验所参考的公开代码见 [ATTRIBUTION.md](ATTRIBUTION.md)。本仓库未为蛋黄形象及动画授予公开再分发或商业使用许可。
