import os
import os.path as osp
import numpy as np
# `pip install easydict` if you don't have it
from easydict import EasyDict as edict
import yaml
import random
__C = edict()
# Consumers can get config by:
#   from fast_rcnn_config import cfg
cfg = __C
'''transformer config'''
__C.MODEL='lwtransformer'
__C.LAYER= 6
__C.HIDDEN_SIZE= 512
__C.FF_SIZE= 2048
__C.MULTI_HEAD= 8
__C.DROPOUT_R= 0.1
__C.FLAT_MLP_SIZE= 512
__C.FLAT_GLIMPSES= 1
__C.FLAT_OUT_SIZE= 512
'''group config'''
__C.EXPAND=1
__C.GROUP=2

# Pixel mean values (BGR order) as a (1, 1, 3) array
# We use the same pixel mean for all networks even though it's not exactly what
# they were trained with
__C.PIXEL_MEANS = np.array([[[102.9801, 115.9465, 122.7717]]])

# For reproducibility
__C.VERSION = str(random.randint(0, 9999999))

# A small number that's used many times
__C.EPS = 1e-14

__C.BATCHSIZE = 64   #batchsize

__C.USE_GLOVE=True

__C.TRAIN = edict()
__C.TRAIN.LR_BASE= 0.0001
__C.TRAIN.MAX_EPOCH = 13
__C.TRAIN.LR_DECAY_LIST=[10,12]
__C.TRAIN.LR_DECAY_R=0.2

__C.TRAIN.WARMUP_EPOCH= 3
__C.TRAIN.OPT='Adam'
__C.TRAIN.OPT_PARAMS= {'betas': '(0.9, 0.98)', 'eps': '1e-9'}

__C.TRAIN.PRETRAINED_MODEL = None
__C.ROOT_DIR = osp.abspath(osp.join(osp.dirname(__file__), '..'))
__C.EVAL_MODEL=osp.join(__C.ROOT_DIR, 'models',__C.MODEL,'best.pkl')
__C.MODEL_DIR=osp.join(__C.ROOT_DIR, 'models',__C.MODEL+'_'+__C.VERSION)
if not os.path.exists(__C.MODEL_DIR):
    os.mkdir(__C.MODEL_DIR)
'''
multi thread for data loader, 
notice: torch is required for multi thread
'''
__C.NUM_WORKERS=8
__C.PIN_MEM=True
# Root directory of project

__C.BBOX_NORMALIZE_MEANS = (0.0, 0.0, 0.0, 0.0)
__C.BBOX_NORMALIZE_STDS = (0.1, 0.1, 0.2, 0.2)


__C.IMDB_NAME = 'refcoco'   # flickr30k, referit, refcoco, refcoco+
__C.FEAT_TYPE = 'bottom-up'   # ss, wfrpn, wofrpn, vgrpn, bu
__C.USE_KLD = True
__C.USE_REG = True


# __C.BASE_MODEL = 'VGG16'  # res101, VGG16

# genome based
# genome_concat_kld, genome_concat, genome_concat_soft, genome_concat_softreg
# vgg based
# vgg_concat, vgg_concat_soft, vgg_concat_softreg
__C.PROJ_NAME = 'genome'
if __C.USE_KLD:
  __C.PROJ_NAME += '_kld'
else:   #softmax
  __C.PROJ_NAME += '_soft'
if __C.USE_REG:   # bbox regression
  __C.PROJ_NAME += '_reg'

# Data directory
__C.DATA_DIR = osp.join(__C.ROOT_DIR, 'data')

# for selective search
__C.SS_FEAT_DIM = 4096
__C.SS_BOX_DIR = osp.join(__C.DATA_DIR, 'ss_box')
__C.SS_FEAT_DIR = osp.join(__C.DATA_DIR, 'ss_feat_vgg_det')

__C.RPN_TOPN = 100
# 2048 for res101, 4096 for VGG16
__C.BOTTOMUP_FEAT_DIM = 2048

__C.SPT_FEAT_DIM = 5

__C.FEAT_DIR = osp.join(__C.DATA_DIR, 'train2014')
__C.IMAGE_DIR = osp.join(__C.DATA_DIR, 'mscoco/images/train2014')
__C.QUERY_DIR = osp.join(__C.DATA_DIR, __C.IMDB_NAME,'query_dict')
__C.ANNO_PATH = osp.join(__C.DATA_DIR,__C.IMDB_NAME, 'format_%s.pkl')

# Model directory
# VGG16, res101
# __C.MODELS_DIR = osp.abspath(osp.join(__C.ROOT_DIR, 'models', __C.IMDB_NAME, __C.FEAT_TYPE, __C.PROJ_NAME))
# if not os.path.exists(__C.MODELS_DIR):
#   os.makedirs(__C.MODELS_DIR)

# __C.SOLVER_PATH = osp.join(__C.MODELS_DIR, 'solver.prototxt')

__C.LOG_DIR = osp.abspath(osp.join(__C.ROOT_DIR, 'log'))

__C.GAMMA = 2


__C.TOPK = 1
__C.TOPN_ROIS = 20
__C.OVERLAP_THRESHOLD = 0.5
__C.VOCAB_SPACE = 'train'

__C.PAD = 0
__C.UNK = 1
__C.BOS = 2
__C.EOS = 3
__C.SP_IDXS = [__C.PAD,__C.UNK,__C.BOS,__C.EOS]

__C.PAD_WORD = '<blank>'
__C.UNK_WORD = '<unk>'
__C.BOS_WORD = '<s>'
__C.EOS_WORD = '</s>'
__C.SP_WORDS = [__C.PAD_WORD,__C.UNK_WORD,__C.BOS_WORD,__C.EOS_WORD]

__C.BBOX_NORMALIZE_TARGETS_PRECOMPUTED = True
__C.BBOX_NORMALIZE_MEANS = (0.0, 0.0, 0.0, 0.0)
__C.BBOX_NORMALIZE_STDS = (0.1, 0.1, 0.2, 0.2)
__C.BBOX_INSIDE_WEIGHTS = (1.0, 1.0, 1.0, 1.0)
__C.THRESHOLD = 0.5


'''question config'''
__C.QUERY_MAXLEN = 15

__C.USE_LSTM = True
__C.DROPOUT_RATIO = 0.3
__C.WORD_EMB_SIZE = 300
__C.RNN_DIM = 1024
__C.DROPFACTOR_RATIO = 0.1



__C.SPLIT_TOK = '+'


def get_models_dir(imdb_name=None):
  if imdb_name is None:
    imdb_name = cfg.IMDB_NAME
  models_dir = osp.join(cfg.ROOT_DIR, 'models', imdb_name, cfg.FEAT_TYPE, cfg.PROJ_NAME)
  if not os.path.exists(models_dir):
    os.makedirs(models_dir)
  return models_dir

def get_solver_path():
  return osp.join(get_models_dir(), 'solver.prototxt')

def print_cfg():
  print('imdb name: %s'%__C.IMDB_NAME)
  print('feat type: %s'%__C.FEAT_TYPE)
  print('proj name: %s'%__C.PROJ_NAME)


def merge_a_into_b(a, b):
    """Merge config dictionary a into config dictionary b, clobbering the
    options in b whenever they are also specified in a.
    """
    if type(a) is not edict:
        return

    for k, v in a.iteritems():
        # a must specify keys that are in b
        if not b.has_key(k):
            raise KeyError('{} is not a valid config key'.format(k))

        # the types must match, too
        old_type = type(b[k])
        if old_type is not type(v):
            if isinstance(b[k], np.ndarray):
                v = np.array(v, dtype=b[k].dtype)
            else:
                raise ValueError(('Type mismatch ({} vs. {}) '
                                'for config key: {}').format(type(b[k]),
                                                            type(v), k))

        # recursively merge dicts
        if type(v) is edict:
            try:
                merge_a_into_b(a[k], b[k])
            except:
                print('Error under config key: {}'.format(k))
                raise
        else:
            b[k] = v

def cfg_from_file(filename):
    """Load a config file and merge it into the default options."""
    with open(filename, 'r') as f:
        yaml_cfg = edict(yaml.load(f))

    merge_a_into_b(yaml_cfg, __C)
