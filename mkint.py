import datatools as dt
import pyperclip

set = dt.DataProcessor(pyperclip.paste())

pyperclip.copy(set.convert().mkInt().unconvert().get())
