import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from yellowbrick.regressor import PredictionError, ResidualsPlot
from yellowbrick.regressor.alphas import AlphaSelection
from yellowbrick.features import Rank1D, Rank2D
from yellowbrick.features.importances import FeatureImportances


def vis_alpha(model, features, target):
    '''

    '''
    vis_alpha = AlphaSelection(model, size=(1080, 720))
    vis_alpha.fit(features, target)
    vis = vis_alpha.poof()
    vis
    return vis


def vis_feat_importance(model, features, target):
    '''

    '''
    fig = plt.figure()
    ax = fig.add_subplot()
    vis_feat_importance = FeatureImportances(model, ax=ax, size=(1080, 720))
    vis_feat_importance.fit(features, target)
    vis = vis_feat_importance.poof()
    vis
    return vis


def vis_residuals(model, features, target):
    '''

    '''
    vis_residuals = ResidualsPlot(model, size=(1080, 720))
    vis_residuals.fit(features, target)
    vis = vis_residuals.poof()
    vis
    return vis


def vis_all(model, features, target):
    '''

    '''
    a = vis_alpha(model, features, target)
    b = vis_feat_importance(model, features, target)
    c = vis_residuals(model, features, target)
