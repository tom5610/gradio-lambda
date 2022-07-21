FROM public.ecr.aws/lambda/python:3.9
RUN pip install pip --upgrade
COPY ./app ${LAMBDA_TASK_ROOT}/app
COPY ./requirements.txt ${LAMBDA_TASK_ROOT}/requirements.txt

RUN python -m pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt

CMD ["app.app.handler"]
