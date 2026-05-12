/* 
*   IAS Badge Script
*   - This script is used to display the IAS badge on the website using Cert ID.
*
*   Developer: ICEF GmbH
*   Created: 2024-05-10
*   Last update: 2024-05-11
*/
console.log('script loaded');
let badgeContainer=document.getElementById('iasBadge');if(badgeContainer){let certNum=badgeContainer.getAttribute('data-account-id');console.log('cert: '+certNum);if(!certNum){console.error('IAS Badge: Cert ID is missing');}let url='https://api2.icef.com/public/account/certificate/'+certNum;fetch(url).then(response=>response.json()).then(data=>{console.log(data);if(!Array.isArray(data.records)){console.warn('Not an IAS Agent');}if(!data.records[0].CDN_link_to_IAS_logo__c){console.warn('No IAS Badge found');}badgeContainer.innerHTML='<a href="https://www.icef.com/agency/'+data.records[0].Master_Account__c+'" target="_blank" ><img src="'+data.records[0].CDN_link_to_IAS_logo__c+'" alt="logo" style="width: 120px;"></a>';}).catch(error=>{console.error('Error:',error);});}
