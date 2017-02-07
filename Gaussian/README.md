#### ガウシアンフィルタ Gaussian Blur<br>
### Gaussian Blur
- 写真にノイズ(小さな変則的な要素)が多くある場合、ガウスぼかしを使用し、画像の前処理する。

画像内の各ピクセルを正方形(n*n)のカーネルでたたみ込むことで変換する。(全ピクセルに対し周囲のピクセルを考慮し平均値を出すことでなめらかなぼかしを表現する)

標準偏差σのガウシアンぼかしとは、n次元の入力画像A[i,j...]に対してn次元のガウス関数
$$
G_\sigma(x,y,...)= \frac{1}{(\sqrt{2π\sigma^2})}exp(-\frac{r^2}{2\sigma^2})(ここでr^2=x^2+y^2+...)
$$
の畳み込み和
$$
O(r^n_cutoff)
B[i,j,...]=\sum _{x,y,...\in Z^n} G\sigma(x,y,...)A[i-x,j-y,...]
$$
をとることである

$$
ガウス関数は中心から離れるにつれ値が小さくなり、r_{cutoff} ~ 3\sigma程度で打つきり行列を作る。n次元ガウス関数はnこの一次元ガウス関数の直積によって表されることにより、ピクセルあたりの計算量を
$$
$$
O(r^n_{cutoff})
$$
から
$$
O(nr_{cutoff})
$$
とぼかし処理を高速化することができる。


blurGaussian01.py<br>
![screen shot 2017-02-07 at 06 39 34](https://cloud.githubusercontent.com/assets/17031124/22667338/b89534a8-ecff-11e6-8005-7600ac1ff983.png)<br>

blurGaussian02.py<br>
![screen shot 2017-02-07 at 07 19 36](https://cloud.githubusercontent.com/assets/17031124/22668781/5eea668e-ed05-11e6-92aa-c48fe46884d5.png)<br>