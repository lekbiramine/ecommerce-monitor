# test_storage.py
from storage import save_current_products, append_price_history

# Example product data (mock data similar to what parser.py would return)
sample_products = [
    {
        "title": "Lenovo IdeaPad 1 15IJL7",
        "price": "$369.00",
        "comparison_price": "$738.00",
        "brand": "Lenovo",
        "variations": []
    },
    {
        "title": "Dell Inspiron 15",
        "price": "$499.00",
        "comparison_price": None,
        "brand": "Dell",
        "variations": []
    }
]

# File paths for testing
current_file = "data/test_current_products.xlsx"
history_file = "data/test_history.xlsx"

# Test saving the current snapshot
save_current_products(sample_products, current_file)
print(f"Saved current products to {current_file}")

# Test appending to history
append_price_history(sample_products, history_file)
print(f"Appended products to history at {history_file}")

# Saved current products to data/test_current_products.xlsx
# Traceback (most recent call last):
#   File "d:\ecommerce_monitor\storage\test.py", line 31, in <module>
#     append_price_history(sample_products, history_file)
#     ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "d:\ecommerce_monitor\storage\storage.py", line 113, in append_price_history     
#     df_final.to_excel(path, index=False, engine="openpyxl")
#     ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "D:\ecommerce_monitor\venv\Lib\site-packages\pandas\util\_decorators.py", line 333, in wrapper
#     return func(*args, **kwargs)
#   File "D:\ecommerce_monitor\venv\Lib\site-packages\pandas\core\generic.py", line 2439, in to_excel
#     formatter.write(
#     ~~~~~~~~~~~~~~~^
#         excel_writer,
#         ^^^^^^^^^^^^^
#     ...<6 lines>...
#         engine_kwargs=engine_kwargs,
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "D:\ecommerce_monitor\venv\Lib\site-packages\pandas\io\formats\excel.py", line 952, in write
#     writer._write_cells(
#     ~~~~~~~~~~~~~~~~~~~^
#         formatted_cells,
#         ^^^^^^^^^^^^^^^^
#     ...<3 lines>...
#         freeze_panes=freeze_panes,
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "D:\ecommerce_monitor\venv\Lib\site-packages\pandas\io\excel\_openpyxl.py", line 486, in _write_cells
#     for cell in cells:
#                 ^^^^^
#   File "D:\ecommerce_monitor\venv\Lib\site-packages\pandas\io\formats\excel.py", line 890, in get_formatted_cells
#     cell.val = self._format_value(cell.val)
#                ~~~~~~~~~~~~~~~~~~^^^^^^^^^^
#   File "D:\ecommerce_monitor\venv\Lib\site-packages\pandas\io\formats\excel.py", line 607, in _format_value
#     raise ValueError(
#     ...<3 lines>...
#     )
# ValueError: Excel does not support datetimes with timezones. Please ensure that datetimes are timezone unaware before writing to Excel.