import argparse
from collections import OrderedDict

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default="input.txt")
args = parser.parse_args()

def main() -> None:
    """テキストを読み込み、条件を満たす値を出力する関数。

    複数の(整数i , 文字列s)のペアと一つの整数mを読み込み、
    mがiの倍数であるsを、iの小さい順に結合したものを出力する。

    """
    # ファイルを開き、ペア部分と整数m部分を取得
    path = args.input  # コマンドライン引数inputを取得
    with open(path, mode="r") as f:
        pairs = [f.strip() for f in f.readlines()]
        m = int(pairs[-1])
        pairs = [f.split(":") for f in pairs[:-1]]  # 最後尾を除いて、":"で分割

    # mがiの倍数となるペアが各key, valueとなる辞書作成
    pairs_new = {}
    for i, s in pairs:
        i = int(i)
        if m % i == 0:
            pairs_new[i] = s

    # iが小さい順に並べ替えて、全mを文字列として結合
    pairs_new = OrderedDict(
        sorted(pairs_new.items(), key=lambda x: x[0])
    )
    out = "".join(pairs_new.values())

    # 結合したものが空白でなければそれを、空白であればmを出力
    if out != "":
        print(out)
    else:
        print(m)


if __name__ == "__main__":    
    main()
