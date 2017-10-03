function Get-History {            
[CmdletBinding()]            
param ()            
            

$shell = New-Object -ComObject Shell.Application          
$history = $shell.NameSpace(34) 
$folder = $history.Self       
            
$history.Items() |          
foreach {            
 if ($_.IsFolder) {           
   $siteFolder = $_.GetFolder         
   $siteFolder.Items() |        
   foreach {            
     $site = $_             
     if ($site.IsFolder) {           
        $pageFolder  = $site.GetFolder         
        $pageFolder.Items() |        
        foreach {            
           $visit = New-Object -TypeName PSObject -Property @{           
               Place = $($site.Name)           
               URL = $($pageFolder.GetDetailsOf($_,0))           
               Date = $( $pageFolder.GetDetailsOf($_,2))     
           }
           $visit
        }            
     }            
   }            
 }            
}     
}    