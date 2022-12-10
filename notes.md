## Tensorflow Stuff
### Saving models in SavedModel Format
- https://www.tensorflow.org/guide/saved_model#creating_a_savedmodel_from_keras
- NOTE: Tensorflow SavedModels should be in the model leaf format /models/model_name/1

## Building TF Serving Containers
- https://www.tensorflow.org/install/docker
- https://www.tensorflow.org/tfx/serving/docker
- https://www.tensorflow.org/tfx/serving/serving_kubernetes
### Container endpoints
Rest API: https://www.tensorflow.org/tfx/serving/api_rest
- curl -X GET http://localhost:8501/v1/models/bert_base_uncased - returns model status
- + /metadata - returns metadata


## Environment
### Does it make sense to use Conda & Poetry?
- https://stackoverflow.com/questions/70851048/does-it-make-sense-to-use-conda-poetry

### VSCode
- conda install -n base_env ipykernel --update-deps --force-reinstall

### Mac OSx environemnt 
- https://stackoverflow.com/questions/65415996/how-to-specify-the-architecture-or-platform-for-a-new-conda-environment-apple