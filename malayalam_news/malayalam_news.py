import csv
import os

import datasets


_DESCRIPTION = """\
The AI4Bharat-IndicNLP dataset is an ongoing effort to create a collection of large-scale, 
general-domain corpora for Indian languages. Currently, it contains 2.7 billion words for 10 Indian languages from two language families. 
We share pre-trained word embeddings trained on these corpora.
We create news article category classification datasets for 9 languages to evaluate the embeddings.
We evaluate the IndicNLP embeddings on multiple evaluation tasks.
"""

_CITATION = """\
@article{kunchukuttan2020indicnlpcorpus,
    title={AI4Bharat-IndicNLP Corpus: Monolingual Corpora and Word Embeddings for Indic Languages},
    author={Anoop Kunchukuttan and Divyanshu Kakwani and Satish Golla and Gokul N.C. and Avik Bhattacharyya and Mitesh M. Khapra and Pratyush Kumar},
    year={2020},
    journal={arXiv preprint arXiv:2005.00085},
}
"""

# "malayalam_news": "https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/evaluations/classification/indicnlp-news-articles.tgz"
_URLs = {
    "malayalam_news": "https://huggingface.co/datasets/rajeshradhakrishnan/malayalam_news/resolve/main/indicnlp-news-articles.tgz"
}

class MalayalamNewsConfig(datasets.BuilderConfig):
    """BuilderConfig for MalayalamNews."""

    def __init__(self, **kwargs):
        """BuilderConfig for MalayalamNews.

        Args:
            **kwargs: keyword arguments forwarded to super.
        """
        super(MalayalamNewsConfig, self).__init__(**kwargs)

class MalayalamNews(datasets.GeneratorBasedBuilder):
    """Malayalam News topic classification dataset."""

    VERSION = datasets.Version("1.0.0")

    BUILDER_CONFIGS = [
        MalayalamNewsConfig(
            name="malayalam_news", version=VERSION, description="Malayalam News topic classification dataset."
        ),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "text": datasets.Value("string"),
                    "label": datasets.features.ClassLabel(names=["business", "entertainment", "sports", "technology"]),
                }
            ),
            homepage="https://github.com/AI4Bharat/indicnlp_corpus#indicnlp-news-article-classification-dataset",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        download_url = _URLs[self.config.name]
        data_dir = dl_manager.download_and_extract(download_url)
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={
                    "filepath": os.path.join(data_dir, "indicnlp-news-articles", "ml", "ml-train.csv"),
                    "split": "train",
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                gen_kwargs={
                    "filepath": os.path.join(data_dir, "indicnlp-news-articles", "ml", "ml-valid.csv"),
                    "split": "validation",
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                gen_kwargs={
                    "filepath": os.path.join(data_dir, "indicnlp-news-articles", "ml", "ml-test.csv"),
                    "split": "test",
                },
            )
        ]

    def _generate_examples(self, filepath, split):
        """Generate Malayalam News examples."""
        with open(filepath, encoding="utf-8") as csv_file:
            csv_reader = csv.reader(
                csv_file, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True
            )
            for id_, row in enumerate(csv_reader):
                label, description = row
                #label, title, description = row
                # Original labels are [1, 2, 3, 4] ->
                #                   ['World', 'Sports', 'Business', 'Sci/Tech']
                # Re-map to [0, 1, 2, 3].
                #label = int(label) - 1
                #text = " ".join((title, description))
                text = description
                yield id_, {"text": text, "label": label}