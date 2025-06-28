df = pd.read_csv('Negara.csv', index_col=0)

rata_rataPopulasi = df.Populasi.mean()
perbedaan_luas_wilayah_antar_negara = df.Luas.std()

print(df)
print("Rata-rata populasi negara didalam data:",rata_rataPopulasi)
print("Simpangan baku luas negara didalam data:",perbedaan_luas_wilayah_antar_negara)
