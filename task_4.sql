SELECT 
    TABLE_SCHEMA AS 'Database',
    TABLE_NAME AS 'Table',
    COLUMN_NAME AS 'Column',
    ORDINAL_POSITION AS 'Position',
    COLUMN_DEFAULT AS 'Default',
    IS_NULLABLE AS 'Nullable',
    DATA_TYPE AS 'Data Type',
    CHARACTER_MAXIMUM_LENGTH AS 'Max Length',
    COLUMN_TYPE AS 'Column Type',
    COLUMN_KEY AS 'Key',
    EXTRA AS 'Extra',
    COLUMN_COMMENT AS 'Comment'
FROM information_schema.columns
WHERE TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'books'
ORDER BY ORDINAL_POSITION;
