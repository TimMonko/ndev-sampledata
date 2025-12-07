"""
This module is an example of a barebones sample data provider for napari.

It implements the "sample data" specification.
see: https://napari.org/stable/plugins/building_a_plugin/guides.html#sample-data

Replace code below according to your needs.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from bioio_imageio import Reader as ImageIOReader
from bioio_ome_tiff import Reader as OmeTiffReader
from ndevio import nImage

if TYPE_CHECKING:
    from napari.types import LayerDataTuple

sample_dir = Path(__file__).parent / "samples"


def ndev_logo() -> list[LayerDataTuple]:
    return nImage(
        sample_dir / "ndev-logo.png",
        reader=ImageIOReader,
    ).get_layer_data_tuples()


def scratch_assay() -> list[LayerDataTuple]:
    img = nImage(
        sample_dir / "scratch-assay-labeled-10T-2Ch.tiff",
        reader=OmeTiffReader,
    )
    return img.get_layer_data_tuples(
        in_memory=True,
        channel_types={
            "H3342": "image",
            "oblique": "image",
            "nuclei": "labels",
            "cyto": "labels",
        },
        channel_kwargs={
            "H3342": {"colormap": "cyan"},
            "oblique": {"colormap": "gray"},
        },
    )


def neocortex() -> list[LayerDataTuple]:
    return nImage(
        sample_dir / "neocortex-3Ch.tiff",
        reader=OmeTiffReader,
    ).get_layer_data_tuples(in_memory=True)


def neuron_raw() -> list[LayerDataTuple]:
    # use pooch to get the download from remote URL if not present locally
    import pooch

    neuron_raw_path = pooch.retrieve(
        url="doi:10.5281/zenodo.17836129/neuron-4Ch_raw.tiff",
        known_hash="md5:5d3e42bca2085e8588b6f23cf89ba87c",
        fname="neuron-4Ch_raw.tiff",
        path=sample_dir,
    )
    return nImage(
        neuron_raw_path,
        reader=OmeTiffReader,
    ).get_layer_data_tuples(
        in_memory=True,
        layer_type="image",
        channel_kwargs={
            "PHALL": {"colormap": "gray"},
        },
    )


def neuron_labels() -> list[LayerDataTuple]:
    return nImage(
        sample_dir / "neuron-4Ch_labels.tiff",
        reader=OmeTiffReader,
    ).get_layer_data_tuples(
        in_memory=True,
        layer_type="labels",
    )


def neuron_labels_processed() -> list[LayerDataTuple]:
    return nImage(
        sample_dir / "neuron-4Ch_labels_processed.tiff",
        reader=OmeTiffReader,
    ).get_layer_data_tuples(
        in_memory=True,
        layer_type="labels",
    )
