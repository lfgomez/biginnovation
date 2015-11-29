{
gROOT->SetBatch(kTRUE);
TTree *RAW = new TTree("RAW","RAW information");
RAW->ReadFile("last-001.csv");
TCanvas *c1=new TCanvas("c1","c1",800,600); 
RAW->Draw("Var1:TimeStamp>>htemp","","*");
htemp->SetMarkerStyle(20);
htemp->SetTitle("Resultado com as ultimas 100 medidas");
htemp->GetXaxis()->SetTitle("Tempo [UnixTime - s]");
htemp->GetYaxis()->SetTitle("Temperatura [Nao calibrada]");
//Inserir aqui o teste de Chi Quadrado
htemp->Fit("pol1");
c1->Print("last-result.gif");
}
