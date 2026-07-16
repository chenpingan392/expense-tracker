# Expense Tracker

一个使用 Python 开发的个人记账程序。

## 功能

- 添加收入和支出记录
- 使用 JSON 永久保存数据
- 从 JSON 恢复交易记录
- 导出 CSV 表格
- 使用类型标注
- 使用虚拟环境管理依赖

## 项目结构

- `app/models.py`：交易数据模型
- `app/storage.py`：JSON 和 CSV 文件操作
- `app/main.py`：程序入口
- `data/`：本地数据文件
- `exports/`：CSV 导出文件
- `tests/`：自动化测试

## 运行方法

```powershell
python -m app.main