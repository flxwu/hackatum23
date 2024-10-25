"""import LogInput
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import requests
import logging
import contextlib
from http.client import HTTPConnection
import json"""


def split_context(context, overlap=50, max_length=4096):
    """
    Function for splitting context into overlapping chunks.

    param context: This is the text that you want to split into chunks. 
    The function will split this text based on the max_length and overlap parameters.

    param overlap (default=50): This is the number of characters that will overlap between each chunk. 
    This is used to ensure that the context is not cut off in the middle of a sentence, which could make the text difficult to understand.

    param max_length (default=512): This is the maximum length of each chunk. 
    The function will split the context into chunks of this length, with the exception of the last chunk, which may be shorter.

    The function returns a list of chunks, where each chunk is a string of text from the context. 
    The chunks are created by starting at the beginning of the context and moving forward max_length
    characters at a time, with an overlap of overlap characters between each chunk.
    """

    chunks = []
    start = 0
    while start < len(context):
        end = min(start + max_length, len(context))
        chunks.append(context[start:end])
        if end == len(context):
            break
        start = end - overlap
    return chunks


def summarize(context):
    return context[:50]


# def summarize_summaries(input=LogInput.get_log_input()):
def summarize_summaries(input):
    chunks = split_context(input)

    outputs = []
    for chunk in chunks:
        outputs.append(summarize(chunk))

    # 4096/512 = 8
    # number of new chunks: len(outputs)/8

    while len(outputs) > 1:
        number_chunks = (len(outputs)/8) + 1
        outputs_temp = []
        for i in number_chunks:
            outputs_temp.append(summarize("".join(outputs[i:i+8])))
        outputs = outputs_temp

    return outputs[0]


summarize_summaries("""germany,[e] officially the Federal Republic of Germany,[f] is a country in the western region of Central Europe. It is the second-most populous country in Europe after Russia, and the most populous member state of the European Union. Germany is situated between the Baltic and North seas to the north, and the Alps to the south. Its 16 constituent states are bordered by Denmark to the north, Poland and the Czech Republic to the east, Austria and Switzerland to the south, and France, Luxembourg, Belgium, and the Netherlands to the west. The nation's capital and most populous city is Berlin and its main financial centre is Frankfurt; the largest urban area is the Ruhr.

Various Germanic tribes have inhabited the northern parts of modern Germany since classical antiquity. A region named Germania was documented before AD 100. In 962, the Kingdom of Germany formed the bulk of the Holy Roman Empire. During the 16th century, northern German regions became the centre of the Protestant Reformation. Following the Napoleonic Wars and the dissolution of the Holy Roman Empire in 1806, the German Confederation was formed in 1815.

Formal unification of Germany into the modern nation-state was commenced on 18 August 1866 with the North German Confederation Treaty establishing the Prussia-led North German Confederation later transformed in 1871 into the German Empire. After World War I and the German Revolution of 1918–1919, the Empire was in turn transformed into the semi-presidential Weimar Republic. The Nazi seizure of power in 1933 led to the establishment of a totalitarian dictatorship, World War II, and the Holocaust. After the end of World War II in Europe and a period of Allied occupation, in 1949, Germany as a whole was organized into two separate polities with limited sovereignty: the Federal Republic of Germany, generally known as West Germany, and the German Democratic Republic, known as East Germany, while Berlin continued its de jure Four Power status. The Federal Republic of Germany was a founding member of the European Economic Community and the European Union, while the German Democratic Republic was a communist Eastern Bloc state and member of the Warsaw Pact. After the fall of communist led-government in East Germany, German reunification saw the former East German states join the Federal Republic of Germany on 3 October 1990.

Germany has been described as a great power with a strong economy; it has the largest economy in Europe, the world's third-largest economy by nominal GDP and the fifth-largest by PPP. As a global power in industrial, scientific and technological sectors, it is both the world's third-largest exporter and importer. As a developed country it offers social security, a universal health care system and a tuition-free university education. Germany is a member of the United Nations, European Union, NATO, Council of Europe, G7, G20, and OECD. It has the third-greatest number of UNESCO World Heritage Sites.
                    """)
