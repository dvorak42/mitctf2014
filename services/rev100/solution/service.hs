main = sunCore 13

rotn n s = map rotchar s 
    where rotchar c = maybe '#' id (lookup c transp)
          transp = zip letters ((drop n letters) ++ (take n letters))
          letters = ['A' .. 'Z']


sunCore a = putStrLn $ rotn a "tesseract2014{ThereBeStringsInThisBinary}"
