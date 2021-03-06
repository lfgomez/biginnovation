{
gROOT->SetBatch(kTRUE);
TTree *RAW = new TTree("RAW","RAW information");
RAW->ReadFile("001.csv");
TCanvas *c1=new TCanvas("c1","c1",800,600); 
RAW->Draw("Var1:TimeStamp>>htemp","","L*");
htemp->SetMarkerStyle(20);
htemp->SetTitle("Resultado com todos os dados");
htemp->GetXaxis()->SetTitle("Tempo [UnixTime - s]");
htemp->GetYaxis()->SetTitle("Temperatura [Nao calibrada]");
c1->Print("result.gif");
}
