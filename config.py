import torch
class PruneConfig(object):
    def __init__(self):
        self.n_points_per_layer = 1
        self.prunable_layer_types = [torch.nn.modules.conv.Conv2d, torch.nn.modules.linear.Linear]
        self.calib_batch = 20
        self.device = 'cuda'
        self.policy = None
        self.fmap_save = True
        self.fmap_save_path = './'


class LassoPruneConfig(PruneConfig):
    def __init__(self, model, ckpt, train_dataloader, pruner="lasso",  val_dataloader=None, criterion=None, policy=None):
        super(LassoPruneConfig, self).__init__()
        self.model = model
        self.ckpt = ckpt
        self.train_dataloader = train_dataloader
        self.val_dataloader = val_dataloader
        self.criterion = criterion
        self.policy = policy
        self.pruner = pruner
