WORKSPACE_PATH = 'Tensorflow/workspace'
SCRIPTS_PATH = 'Tensorflow/scripts'
APIMODEL_PATH = 'Tensorflow/models'
ANNOTATION_PATH = WORKSPACE_PATH+'/annotations'
IMAGE_PATH = WORKSPACE_PATH+'/images'
MODEL_PATH = WORKSPACE_PATH+'/models'
PRETRAINED_MODEL_PATH = WORKSPACE_PATH+'/pre-trained-models'
CONFIG_PATH = MODEL_PATH+'/my_ssd_mobnet/pipeline.config'
CHECKPOINT_PATH= MODEL_PATH+'/my_ssd_mobnet'

def main():
    labels = [
        {'name':'1', 'id':1},
        {'name':'2', 'id':2},
        {'name':'3', 'id':3},
        {'name':'4', 'id':4},
        {'name':'5', 'id':5},
    ]

if __name__ == "__main__":
    main()