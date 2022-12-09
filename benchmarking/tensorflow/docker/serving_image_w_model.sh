#Pull Tensorflow Serving Images
docker pull tensorflow/serving

# Run the serving image
docker run -d --name serving_base tensorflow/serving

#Copy your SavedModel to the container's model folder:
docker cp ./models/bert serving_base:/models/bert