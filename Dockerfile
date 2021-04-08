# Set Python version
FROM python:3.7

# Copy entire project
COPY . /app
WORKDIR /app

# Install requirements
RUN pip3 install -r requirements.txt

# Clear port to run app
EXPOSE 80

# Copy Streamlit conditions not needed anymore as there are found in App folder
# RUN mkdir ~/.streamlit
# RUN cp config.toml ~/.streamlit/config.toml
# RUN cp credentials.toml ~/.streamlit/credentials.toml

# Go into the dashboard folder
WORKDIR /app/App

# Run unit testing on front-end application
RUN python -m pytest App/Testing/

# Run app using streamlit run app.py
ENTRYPOINT ["streamlit", "run", "app.py"]
