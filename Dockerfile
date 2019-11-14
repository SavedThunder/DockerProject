FROM python:3.7-alpine

COPY "cc_project.py" .

run mkdir 'home/output'

CMD ["python" , "./cc_project.py"]

