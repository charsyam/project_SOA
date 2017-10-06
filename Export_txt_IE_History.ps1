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
               $($site.Name)+ ' : '+ $($pageFolder.GetDetailsOf($_,0)) + ' : ' + $( $pageFolder.GetDetailsOf($_,2))
        }            
     }            
   }            
 }            
}     
}    