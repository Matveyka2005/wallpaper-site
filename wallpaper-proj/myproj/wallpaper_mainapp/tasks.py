from myproj.celery import app


@app.task
def some_task():
    return True
