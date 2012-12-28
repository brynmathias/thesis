#!/usr/bin/env python
import ROOT as r
from plottingUtils import Print
import array
def main():
    c1 = Print("transFac.pdf")
    c1.DoPageNum = False
    h = r.TH1D("","",1000,0.,1000.)
    xbins = [275.,325,] + [375 + i*100 for i in range(6)]
    transFac = [ 2.34,2.06,2.10,2.18,2.01,2.45,2.48,2.54]
    transFacErr = [0.1,0.14,0.04,0.16,0.16,0.25,0.33,0.40]
    h = h.Rebin(len(xbins)-1,"",array.array('d',xbins))
    
    for b in range(0,h.GetNbinsX()+1):
        h.SetBinContent(b,transFac[b])
        h.SetBinError(b,transFacErr[b])
    h.GetXaxis().SetTitle("H_{T} (GeV)")
    h.GetYaxis().SetTitleSize(h.GetXaxis().GetTitleSize())
    h.GetYaxis().SetTitle("Translation Factor")
    h.Draw()
    c1.canvas.Update()
    raw_input()
    # Do pol0 fit here by hand in the root interface.
    c1.Print()
    c1.close()



if __name__ == '__main__':
    main()