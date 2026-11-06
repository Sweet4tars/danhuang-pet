# 安装蛋黄 · 摸摸爱心版

本文件供接收电脑的 Codex 阅读。用户要求安装本包时，按以下范围执行。

1. 解压完整压缩包并阅读 install.py、manifest.json。核对 SHA256SUMS 中的每个文件，以及 manifest.json 中两个宠物文件的大小和 SHA-256。
2. 确定目标电脑实际使用的 CODEX_HOME，未自定义时为用户目录下 .codex。使用 Python 3 运行 install.py --verify，再运行 install.py；自定义目录传入 --codex-home 实际路径。
3. 安装工具仅写入 <CODEX_HOME>/pets/danhuang/。已有不同版本会完整备份到 <CODEX_HOME>/pet-backups/danhuang/时间戳/，相同版本无需重复写入。不要删除其他宠物。
4. 核对安装后的 pet.json 和 spritesheet.webp 与包内一致。spriteVersionNumber 应为 2。
5. 通过可用的官方宠物选择入口刷新并选择本次安装的蛋黄；缺少选择工具时明确告知用户手动选择，不要声称已激活。
6. 若当前为已迁移云端宠物，保留原稳定 ID，使用受支持的 Pets 图片更新接口更新该条目。缺少接口时，只报告本地安装状态与云端尚未替换，不要通过修改缓存、强制配置或擅自创建重复宠物来冒充成功。
7. 按 动作与触发说明.md 实测鼠标进入身体区域时的摸摸爱心与恢复坐姿。只有实际客户端显示后，才报告新悬停动作已生效。

本包无需 GitHub 登录、网络或图像生成。报告安装位置、校验结果、备份位置（如有）以及本地/云端实际显示状态。
