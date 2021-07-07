import MeCab
class Morphological_analysis:
    @classmethod
    def morphological_analysis(self,message):
        res = message
        tagger = MeCab.Tagger("-u add_dic")
        parsed_txt = tagger.parse(res)
        elements = parsed_txt.split("\n")[:-2]

        results = []
        for element in elements:
            parts = element.split(",")
            surface_pos, pos1, pos2, pos3, base = parts[0], parts[1], parts[2], parts[3], parts[-3]
            surface, pos = surface_pos.split("\t")
            results.append(dict(表層形=surface,基本形=base,品詞=pos,品詞1=pos1,品詞2=pos2,品詞3=pos3))

       # 単語の取り出し
        for result in results:
            if result["品詞"] == "名詞" and result["品詞1"] == "固有名詞" and result["品詞2"] == "人名" and result["品詞3"] == "一般": 
                def_search_word = result["表層形"]

        try:
            return def_search_word
        except UnboundLocalError:
            return "私にはわかりません。別の質問なら何とか答えられるかもしれません。"