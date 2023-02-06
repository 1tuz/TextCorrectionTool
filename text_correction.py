import textacy

def correct_text(text):
    # Use TextaCy to process the text
    doc = textacy.make_spacy_doc(text, lang='en')
    
    # Use TextaCy's built-in spelling correction
    corrected_text = textacy.preprocess.normalize.normalize_whitespace(doc._.text)
    corrected_text = textacy.preprocess.normalize.normalize_unicode(corrected_text)
    corrected_text = textacy.preprocess.normalize.normalize_quotation_marks(corrected_text)
    corrected_text = textacy.preprocess.normalize.normalize_contractions(corrected_text)
    corrected_text = textacy.preprocess.normalize.normalize_acronyms(corrected_text)
    
    # Return the corrected text
    return corrected_text
