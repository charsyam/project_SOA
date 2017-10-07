function Get-History {            
[CmdletBinding()]            
param ()            

$env:hostIP = (Get-NetIPConfiguration | Where-Object { $_.IPv4DefaultGateway -ne $null -and $_.netadapter.status -ne "Disconnected"}).ipv4address.ipaddress 
$env:hostMAC = (Get-NetAdapter | where-object -FilterScript {$_.HardwareInterface -eq "True" -and $_.Status -ne "Disconnected"}).MacAddress 

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
               $env:userdomain + " : " + $env:COMPUTERNAME + " : " + $($env:hostIP) + ' : ' +    
               $($env:hostMAC) + ' : ' + $env:username + " : "  + $($pageFolder.GetDetailsOf($_,2)).replace(' ', " : ") + ' : ' +
               $($site.Name).replace("내 PC", "") + ' : ' +$($pageFolder.GetDetailsOf($_,0)).replace("file:///", "") + ' : ' + $($pageFolder.GetDetailsOf($_,1))  | out-file C:\Users\Public\Documents\${env:COMPUTERNAME}_$(get-date -f yyyyMMddhhmm)_IEhistory.txt -Append
        }            
     }            
   }            
 }            
}     
}    