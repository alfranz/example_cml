import papermill
import os
import logging

def report():
    load_path = "report.ipynb"
    save_path = "report.output.ipynb"
    output = papermill.execute_notebook(
        load_path, save_path, report_mode=True, nest_asyncio=True, kernel_name='python'
    )
    exception = output["metadata"]["papermill"]["exception"]
    status_code = os.system("jupyter nbconvert --to markdown report.output.ipynb --no-input")

    if not exception and status_code == 0:
        logging.info("Validation notebook ran successfully.")
    else:
        logging.warning(
            "Issue with papermill: {}, issue with nbconvert:{}".format(
                exception, status_code
            )
        )

report()