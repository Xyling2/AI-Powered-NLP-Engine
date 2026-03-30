import spacy
from transformers import pipeline
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NLPEngine:
    """
    A production-grade NLP Engine for processing large-scale text data.
    """
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        logger.info(f"Initializing NLP Engine with model: {model_name}")
        try:
            self.sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)
            self.nlp = spacy.load("en_core_web_sm")
        except Exception as e:
            logger.error(f"Failed to initialize engine: {e}")
            raise

    def process(self, text: str) -> dict:
        """
        Processes the input text and returns a dictionary of NLP insights.
        """
        if not text:
            return {}

        sentiment = self.sentiment_analyzer(text)[0]
        doc = self.nlp(text)
        entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

        return {
            "sentiment": sentiment,
            "entities": entities,
            "text_length": len(text)
        }

if __name__ == "__main__":
    engine = NLPEngine()
    sample_text = "The latest advancements in AI are truly inspiring."
    print(engine.process(sample_text))
