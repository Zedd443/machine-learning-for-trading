# Rulebook V1 — HTF Trend + 15m Pullback Continuation

Status: HIPOTESIS UNTUK DIUJI. Bukan strategi yang dinyatakan profitable.

## Market & timeframe
BTCUSDT dan ETHUSDT perpetual.
Context 1H, execution 15m.

## Risk
0.25%–0.50% equity per trade saat forward test.
Maksimum satu posisi per simbol.
Tidak averaging down.

## Definisi
Swing high: high candle lebih tinggi dari high 2 candle kiri dan 2 kanan.
Swing low: low candle lebih rendah dari low 2 candle kiri dan 2 kanan.
Bull trend 1H: dua swing high lebih tinggi DAN dua swing low lebih tinggi terakhir.
Bear trend: kebalikannya.
Range: tidak memenuhi keduanya.

## Volatility filter
ATR(14) 15m harus berada di percentile 25–90 dari 100 candle sebelumnya. Ini parameter eksperimen, bukan kebenaran.

## Long
1. 1H bull trend.
2. Harga 15m retrace setelah local high baru.
3. Retrace menyentuh/menembus low minimal satu swing 15m sebelumnya lalu close kembali di atas level itu.
4. Signal candle bullish.
5. Pilih satu metode entry untuk seluruh test: open candle berikutnya ATAU midpoint signal candle.
6. Stop di bawah low signal/sweep + buffer 0.1 ATR.
7. Baseline target fixed 1.5R.

## Short
Simetris dengan long.

## No trade
1H range; ATR di luar filter; daily loss limit tercapai; posisi aktif pada simbol sama; data tidak lengkap.

## Guardrail
Maksimum 3 attempt/hari. Stop hari itu pada -1.5R. Tidak ada target profit harian.

## Wajib dicatat
symbol, timestamp, direction, entry, stop, target, exit, fees, realized_R, regime_1h, ATR percentile, setup_valid, rule_violation.

## Dilarang selama test
Memindah stop menjauh; mengubah TP karena feeling; menambah indikator setelah loss; membuang losing trade dari sample karena hindsight.

## Validation
Pilot 30–50 occurrence untuk debugging.
Main backtest target 150+ occurrence jika tersedia.
Holdout periode berbeda.
Robustness: TP 1.3/1.5/1.7R, buffer 0/0.1/0.2 ATR, fee/slippage assumption +50%.

Retain untuk forward test hanya jika expectancy setelah biaya positif, tidak bergantung pada outlier, drawdown masuk toleransi, parameter cukup stabil, dan holdout tidak runtuh total.
