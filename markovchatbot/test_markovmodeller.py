from unittest import TestCase

from chatbot.markovchatbot import markovmodeller
from chatbot.markovchatbot.mmodel.markovmodel import MarkovModel


class Test_Markov_Basics(TestCase):
    basic_text = "Hello I am a robot"
    basic_text_repetition = "Hello I am a robot robot robot"
    basic_text_repetition_normalise = "Hello I am a Robot robot rObOt"
    basic_text_multiple = "Hello I am a robot I kill"
    basic_text_multiple_2 = "you eat you shoot you leave"

    basic_text_full_stop = "Hello I am a robot."

    def test_build_markov_model(self):
        model = markovmodeller.build_markov_model(self.basic_text)
        self.assertIsInstance(model, MarkovModel)
        self.assertEqual(len(model), 5)
        start_node = model.get_start_node()
        self.assertEqual(len(start_node.connections), 1)
        self.assertEqual(len(model.find_node_by_name("i").connections), 1)
        self.assertEqual(len(model.find_node_by_name("am").connections), 1)

    def test_build_markov_model_repetition(self):
        model = markovmodeller.build_markov_model(self.basic_text_repetition)
        self.assertIsInstance(model, MarkovModel)
        self.assertEqual(len(model), 5)
        self.assertEqual(len(model.find_node_by_name("robot").connections), 1)
        self.assertEqual(len(model.find_node_by_name("roBOT").connections), 1)

    def test_build_markov_model_repetition_normalise(self):
        model = markovmodeller.build_markov_model(self.basic_text_repetition_normalise)
        self.assertIsInstance(model, MarkovModel)
        self.assertEqual(len(model), 5)

    def test_build_markov_model_multiple(self):
        model = markovmodeller.build_markov_model(self.basic_text_multiple)
        self.assertIsInstance(model, MarkovModel)
        self.assertEqual(len(model), 6)
        start_node = model.get_start_node()
        self.assertEqual(len(start_node.connections), 1)
        self.assertEqual(len(model.find_node_by_name("i").connections), 2)
        self.assertEqual(len(model.find_node_by_name("am").connections), 1)

    def test_build_markov_model_multiple_2(self):
        model = markovmodeller.build_markov_model(self.basic_text_multiple_2)
        self.assertIsInstance(model, MarkovModel)
        self.assertEqual(len(model), 4)
        start_node = model.get_start_node()
        self.assertEqual(len(start_node.connections), 1)
        self.assertEqual(len(model.find_node_by_name("you").connections), 3)
        self.assertEqual(len(model.find_node_by_name("eat").connections), 1)
        self.assertIsNone(model.find_node_by_name("definitelyNotAWord"))

    def test_build_markov_model_full_stop(self):
        model = markovmodeller.build_markov_model(self.basic_text_full_stop)
        self.assertIsInstance(model, MarkovModel)
        self.assertEqual(len(model), 6)
        start_node = model.get_start_node()
        self.assertEqual(len(start_node.connections), 1)
        self.assertEqual(len(model.find_node_by_name("i").connections), 1)
        self.assertEqual(len(model.find_node_by_name("am").connections), 1)

    def test_basic_random_walk(self):
        model = markovmodeller.build_markov_model(self.basic_text)
        self.assertEqual(len(model), 5)
        walk_string = markovmodeller.get_totally_random_walk(model)
        self.assertEqual("hello i am a robot", walk_string)

    def test_basic_random_walk_2(self):
        model = markovmodeller.build_markov_model(self.basic_text_full_stop)
        self.assertEqual(len(model), 6)
        walk_string = markovmodeller.get_totally_random_walk(model)
        self.assertEqual("hello i am a robot .", walk_string)


class Test_Markov_Multiple(TestCase):
    basic_text = "Hello I am a robot. Hello I am a robot."
    basic_text_cyborg = "Hello I am a robot. Hello I am a robot. heLlO i Am A hUmAn"

    def test_build_markov_model(self):
        model = markovmodeller.build_markov_model(self.basic_text)
        self.assertIsInstance(model, MarkovModel)
        self.assertEqual(len(model), 6)
        start_node = model.get_start_node()
        self.assertEqual(len(start_node.connections), 1)
        self.assertEqual(len(model.find_node_by_name("i").connections), 1)
        self.assertEqual(len(model.find_node_by_name("am").connections), 1)

    def test_build_markov_model_cyborg(self):
        model = markovmodeller.build_markov_model(self.basic_text_cyborg)
        self.assertEqual(len(model), 7)
        start_node = model.get_start_node()
        self.assertEqual(len(start_node.connections), 1)
        self.assertEqual(len(model.find_node_by_name("i").connections), 1)
        self.assertEqual(len(model.find_node_by_name("am").connections), 1)
        self.assertEqual(len(model.find_node_by_name("a").connections), 2)

