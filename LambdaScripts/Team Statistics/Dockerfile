FROM python:3.14.0rc2-alpine3.22
WORKDIR /app
COPY . .
RUN pip install requests
RUN pip install boto3
RUN adduser appuser
RUN chown -R app:app /app
USER appuser
CMD ["python"]