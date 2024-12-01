from datetime import datetime
from typing import Dict

ANTALL_PLASSER = 20
PRIS_PER_MINUTT = 1.5

class Bil:
    def __init__(self, reg_nr, modell, farge):
        self.reg_nr = reg_nr
        self.modell = modell
        self.farge = farge
        self.innkjøringstid = None
        print(f"Opprettet {farge} {modell} med reg.nr. {reg_nr}")

class Lastebil(Bil):
    def __init__(self, reg_nr, modell, farge):
        super().__init__(reg_nr, modell, farge)
        self.er_stor = True
        print(f"Opprettet lastebil {farge} {modell} med reg.nr. {reg_nr}")

    def beregn_parkeringsavgift(self, minutter_parkert):
        return minutter_parkert * PRIS_PER_MINUTT * 2

class PHus:
    def __init__(self):
        self.parkerte_biler = {}
        print(
            f"Opprettet parkingshus med {ANTALL_PLASSER} plasser", end='\n\n')

    def innkjøring(self, bil, tid):
        bil.innkjøringstid = tid
        self.parkerte_biler[bil.reg_nr] = bil
        print(f"{bil.reg_nr} kjørte inn {tid.strftime('%H:%M')}")
        self.vis_ledige_plasser()

    def utkjøring(self, reg_nr, tid):
        bil = self.parkerte_biler.pop(reg_nr)
        minutter_parkert = (tid - bil.innkjøringstid).total_seconds()/60
        if isinstance(bil, Lastebil):
            parkeringsavgift = bil.beregn_parkeringsavgift(minutter_parkert)
        else:
            parkeringsavgift = minutter_parkert * PRIS_PER_MINUTT
        print(
            f"{bil.reg_nr} {bil.farge} {bil.modell} kjørte ut {tid.strftime('%H:%M')}")
        print(
            f"Parkeringstid: {minutter_parkert:.0f} min., avgift kr {parkeringsavgift:.2f}")
        self.vis_ledige_plasser()

    def vis_ledige_plasser(self):
        antall_ledige_plasser = ANTALL_PLASSER - len(self.parkerte_biler)
        print(f'Antall ledige plasser: {antall_ledige_plasser}', end='\n\n')

    def vis_biler_med_farge(self, farge):
        for bil in self.parkerte_biler.values():
            if bil.farge == farge:
                print(f"{bil.reg_nr} {bil.farge} {bil.modell}")

if __name__ == "__main__":
    phus = PHus()

    bil = Bil("AB12345", "Tesla", "rød")
    tid = datetime(2023, 11, 29, 13, 37)
    phus.innkjøring(bil, tid)

    bil = Bil("EK13002", "eGolf", "hvit")
    tid = datetime(2023, 11, 29, 13, 45)
    phus.innkjøring(bil, tid)

    tid = datetime(2023, 11, 29, 14, 41)
    phus.utkjøring("AB12345", tid)

    bil = Bil("TV12345", "Ford", "hvit")
    tid = datetime(2023, 11, 29, 14, 50)
    phus.innkjøring(bil, tid)

    bil = Bil("VD77077", "Ford", "blå")
    tid = datetime(2023, 11, 29, 14, 55)
    phus.innkjøring(bil, tid)

    phus.vis_biler_med_farge("hvit")

    # Opprett en lastebil og kjør den inn
    print()
    lastebil = Lastebil("XY98765", "Volvo", "rød")
    tid = datetime(2023, 11, 29, 15, 0)
    phus.innkjøring(lastebil, tid)

    # Kjør lastebilen ut etter en time
    tid = datetime(2023, 11, 29, 16, 0)
    phus.utkjøring("XY98765", tid)

    # Vis biler med en bestemt farge
    phus.vis_biler_med_farge("rød")