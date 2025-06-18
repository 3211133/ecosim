# Contributor Guidelines

このリポジトリで作業を行う際の指示をまとめます。

## コードスタイル
- Python ファイルはすべて LF 改行とし、末尾に必ず改行を入れてください。
- 変更を加えたら `pytest -q` を実行してテストを確認してください。
- 依存パッケージを追加した場合は `requirements.txt` を更新してください。

## 修正予定箇所
- `direction.py` の `toPosition` はリストに変更してください。
- `goods.py` の `from .goods import goods` 行を削除し、必要なら `from goods import goods` を使用してください。
- `controller.py` のファイル末尾に改行を追加してください。

新しい機能を追加する場合や挙動を変更する場合は、`tests/` 以下に対応するテストを作成してください。
