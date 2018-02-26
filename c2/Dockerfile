FROM gcr.io/google-appengine/python

# Create a virtualenv for dependencies. This isolates these packages from
# system-level packages.
RUN virtualenv /env

# Setting these environment variables are the same as running
# source /env/bin/activate.
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Copy the application's requirements.txt and run pip to install all
# dependencies into the virtualenv.
ADD requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

# Add the application source code.
ADD c2 ./c2
ADD pops ./pops
ADD tests ./tests
ADD manage.py ./manage.py
ADD templates ./templates
ADD static ./static


# Run a WSGI server to serve the application. gunicorn must be declared as
# a dependency in requirements.txt.
CMD gunicorn -b :$PORT c2.wsgi
