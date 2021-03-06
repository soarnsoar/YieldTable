###----
import ROOT

##---ReadYield of a process list
def ReadYield(inputpath,processlist):
	##---Read Total integrals
	myrf=ROOT.TFile.Open(inputpath)

        dict_yield={}

        ##--for each process
        for process in processlist:

                if 'histo_' in process:
                        process=process.replace('histo_','')
                histopath='histo_'+process
                #print histopath
                myhisto=myrf.Get(histopath)
                dict_yield[process]=myhisto.Integral()

        myrf.Close()
        return dict_yield


def CombineYield(dict_yield,dict_combine):
        ##--dict_combine={'combined_process_name':['tocomb1','tocomb2']}
        for proc in sorted(dict_yield):
                for proc_comb in sorted(dict_combine):
                        sumyield=0.
                        for subproc in dict_combine[proc_comb]['list']:
                                this_yield=dict_yield[subproc]
                                sumyield+=this_yield
                        dict_yield[proc_comb]=sumyield*dict_combine[proc_comb]['scale']
        ##--remove old one
        for subproc in sorted(dict_combine[proc_comb]['list']):
                del dict_yield[subproc]

        return dict_yield
##---convert info in dictionary to latex table
###---input dictionary structure is
###   dict = { 'cutname' : { 'proc1':'yield1',...
#               }
#}
##--order of cut and proc follows input cutlist/proclist
def mkTable(proclist,caption,label,input_dict,outputtxt):
        '''
        \begin{table}[h]
        \centering
        \caption{table cation}
        \begin{tabular}{|l|l|l|l|}
        \hline
        Process & cut1              & cut2                 & cut3                 \\ \hline
        proc1   & y11               & y12                  & y13                  \\ 
        proc2   & y21               & y22                  & y23
        \\ \hline
        \end{tabular}
        \label{tab:tablealias}
        \end{table}
        '''
        lines=[]
        catlist=sorted(input_dict)

        cutlist=[]
        for cat in sorted(catlist):
                cutlist+=input_dict[cat]
        
        lines.append('\\begin{table}[h]\n\\centering')
        lines.append('\\caption{'+caption+'}')
        blocks='|'.join(['l']*(len(cutlist)+1))
        lines.append('\\begin{tabular}{|'+blocks+'|}')
        ##--1st row ->cuts
        lines.append('\\hline')
        
        #fistrow='&'.join(cutlist)
        #lines.append('Process &'+fistrow+'\\\\ \\hline')
        '''
        \multicolumn{3}{c|}
        '''
        firstrow='\multirow{2}{*}{Process} &'
        multicolums=['\\multicolumn{'+str(len(input_dict[cat]))+'}{c|}{'+cat+'}' for cat in sorted(catlist) ]
        #+'&\\multicolumn{'+str(len(catlist))+'}'+'&'.join(catlist)+'\\\\ \\cline{2-'+str(len(cutlist)+1)+'}'
        firstrow+='&'.join(multicolums)+'\\\\ \\cline{2-'+str(len(cutlist)+1)+'}'
        lines.append(firstrow)
        lines.append('&'+'&'.join(cutlist)+'\\\\ \\hline')
        
        ##--proc by proc
        for proc in proclist:
                this_line=proc
                for cat in catlist:
                        for cut in input_dict[cat]:
                                this_yield=input_dict[cat][cut][proc]
                                #print "input_dict[cat]",input_dict[cat]
                                this_line+=' &'+str(round(this_yield,2))
                this_line+=' \\\\'
                lines.append(this_line)

        ##--end table
        lines.append('\\hline')
        lines.append('\\end{tabular}')
        lines.append('\\label{'+label+'}')
        lines.append('\\end{table}')
        ##---
        print "--------------START------------"
        for line in lines:
                print line
        print "--------------END------------"


def mkTableUsingLine(inputlines,caption,label,outputtxt):
        '''
        \begin{table}[h]
        \centering
        \caption{table cation}
        \begin{tabular}{|l|l|l|l|}
        \hline
        Process & cut1              & cut2                 & cut3                 \\ \hline
        proc1   & y11               & y12                  & y13                  \\ 
        proc2   & y21               & y22                  & y23
        \\ \hline
        \end{tabular}
        \label{tab:tablealias}
        \end{table}
        '''
        lines=[]
        lines.append('\\begin{table}[h]\n\\centering')
        lines.append('\\caption{'+caption+'}')
        blocks='|'.join(['l']*(len(inputlines[0])))
        lines.append('\\begin{tabular}{|'+blocks+'|}')
        ##--1st row ->cuts
        lines.append('\\hline')
        
        #fistrow='&'.join(cutlist)
        #lines.append('Process &'+fistrow+'\\\\ \\hline')
        '''
        \multicolumn{3}{c|}
        '''
        #firstrow='\multirow{2}{*}{Process} &'
        #multicolums=['\\multicolumn{'+str(len(input_dict[cat]))+'}{c|}{'+cat+'}' for cat in sorted(catlist) ]
        #+'&\\multicolumn{'+str(len(catlist))+'}'+'&'.join(catlist)+'\\\\ \\cline{2-'+str(len(cutlist)+1)+'}'
        #firstrow+='&'.join(multicolums)+'\\\\ \\cline{2-'+str(len(cutlist)+1)+'}'
        #lines.append(firstrow)
        for iline in range(len(inputlines)):
                lines.append('&'.join(inputlines[iline])+'\\\\ \\hline')
        
        ##--proc by proc
        #for nuis in nuislist:
        #        this_line=proc
        #        for cat in catlist:
        #                for cut in input_dict[cat]:
        #                        this_yield=input_dict[cat][cut][proc]
        #                        this_line+=' &'+str(round(this_yield,2))
        #        this_line+=' \\\\'
        #        lines.append(this_line)

        ##--end table
        lines.append('\\hline')
        lines.append('\\end{tabular}')
        lines.append('\\label{'+label+'}')
        lines.append('\\end{table}')
        ##---
        print "--------------START------------"
        for line in lines:
                print line
        print "--------------END------------"

        


##--------sysvar
def ReadYieldVar(inputpath,process,nuisance):
#def ReadYieldVar(inputpathlist,process,nuisance):
	##---Read Total integrals
        dict_yield={}
        myrf=ROOT.TFile.Open(inputpath)
        
        ##--for each process
        
        if 'histo_' in process:
                process=process.replace('histo_','')
        histopath_nom='histo_'+process
        histopath_var='histo_'+process+'_'+nuisance
        
        
        #print histopath
        
        nomhisto=myrf.Get(histopath_nom)
        nom=nomhisto.Integral()
        varhisto=myrf.Get(histopath_var)
        var=varhisto.Integral()


        #dict_yield[process]=myhisto.Integral()

        myrf.Close()
        #return dict_yield
        
        r_var=abs((nom-var)/nom)
        return r_var


def ReadYieldVarProcList(inputpath,processlist,nuisance):
#def ReadYieldVar(inputpathlist,process,nuisance):
	##---Read Total integrals
        dict_yield={}
        myrf=ROOT.TFile.Open(inputpath)
        nom=0.
        var=0.
        ##--for each process
        for process in processlist:
                if 'histo_' in process:
                        process=process.replace('histo_','')
                histopath_nom='histo_'+process
                histopath_var='histo_'+process+'_'+nuisance
        
        
                #print histopath_nom
                #print histopath_var
                
                nomhisto=myrf.Get(histopath_nom)
                nom+=nomhisto.Integral()
        
                varhisto=myrf.Get(histopath_var)
                try:
                        var+=varhisto.Integral()
                except:
                        #print 'no histogram->',histopath_var
                        var+=nomhisto.Integral()
                        pass
                #dict_yield[process]=myhisto.Integral()

        myrf.Close()
        #return dict_yield
        if nom==0 or var==0:
                print "No Shape"
                r_var=0.
        else:
                r_var=abs((nom-var)/nom)
        return r_var
