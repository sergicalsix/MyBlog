### ファイルの削除
- 初めての取り消し(// インデックスからのみ削除し、ファイルはそのまま)
`git rm --cached -r file_name`
- ２回目以降の取り消し
`git reset HEAD file_name`