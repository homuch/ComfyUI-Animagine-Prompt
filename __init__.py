"""
Animagine Prompt Node for ComfyUI
A node designed to help structure prompts according to specific guidelines
"""

import os
import logging
from .animagine_node import AnimaginePromptNode

# Basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('AnimaginePrompt')

# Base directory of the node
NODE_DIR = os.path.dirname(os.path.realpath(__file__))
SAMPLE_DATA_DIR = os.path.join(NODE_DIR, "sample_data")

# Ensure the sample_data directory exists
if not os.path.exists(SAMPLE_DATA_DIR):
    os.makedirs(SAMPLE_DATA_DIR)

# Mapping for node registration
NODE_CLASS_MAPPINGS = {
    "AnimaginePrompt": AnimaginePromptNode
}

# Mapping for display name
NODE_DISPLAY_NAME_MAPPINGS = {
    "AnimaginePrompt": "Animagine Prompt"
}

__version__ = "1.0.1"