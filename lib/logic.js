/**
 * New script file
 */

/**
 * Create Document
 * @param {org.important.mynetwork.createDocument} docDetails  - the document to be created
 * @transaction
 */
function docCreate(docDetails) {
    
    var bank;
    var client;
  	var clientExists = new Boolean(false)
    var bankExists = new Boolean(false)
    var clientRegistry
    var bankRegistry
    return getParticipantRegistry('org.important.mynetwork.Client')
    .then(function (registry){
        clientRegistry = registry
      	return registry.exists(docDetails.clientID)
        	
        })
  	.then(function (exists){
    	clientExists = exists
      return getParticipantRegistry('org.important.mynetwork.Bank')
    })
    .then ( function(registry){
        bankRegistry = registry
      	 return registry.exists(docDetails.bankID)
    })
  	.then(function (exists){
            bankExists = exists
            return clientRegistry.get(docDetails.clientID)
      })
    .then(function(client_temp){
        client = client_temp
        return bankRegistry.get(docDetails.bankID)
    })
    .then(function(bank_temp){
        bank = bank_temp
        return getAssetRegistry('org.important.mynetwork.ClientDocument')
    })
    .then(function ( registry){
        if((clientExists == true) && (bankExists == true)){
      	var factory = getFactory();
        var newOrder = factory.newResource('org.important.mynetwork','ClientDocument',docDetails.documentID);

        newOrder.documents = docDetails.documents;
        newOrder.ownerClient = client;
        newOrder.ownerBank = bank;
        return registry.add(newOrder);
        }
    })
    .catch(function (err){
        throw new Error (err);
    });
}

/**
 * Create Bank
 * @param {org.important.mynetwork.createBank} bank  - the Bank to be created
 * @transaction
 */

 function bankCreate (bank){

    return getParticipantRegistry('org.important.mynetwork.Bank')
    .then (function(registry){
        var factory = getFactory();
        var newOrder = factory.newResource('org.important.mynetwork','Bank',bank.id);
        newOrder.bankName = bank.name;
        return registry.add(newOrder);
    })
    .catch(function (err){
        throw new Error(err);
    });
 }

/**
 * Create Client
 * @param {org.important.mynetwork.createClient} client  - the client to be created
 * @transaction
 */

function clientCreate (client){

    return getParticipantRegistry('org.important.mynetwork.Client')
    .then (function(registry){
        var factory = getFactory();
        var newOrder = factory.newResource('org.important.mynetwork','Client',client.id);
        newOrder.clientName = client.name;
        return registry.add(newOrder);
    })
    .catch(function (err){
        throw new Error(err);
    });
 }


/**
 * Create Verifier
 * @param {org.important.mynetwork.createVerifier} verifier  - the verifier to be created
 * @transaction
 */

function verifierCreate (verifier){

    return getParticipantRegistry('org.important.mynetwork.Verifier')
    .then (function(registry){
        var factory = getFactory();
        var newOrder = factory.newResource('org.important.mynetwork','Verifier',verifier.id);
        newOrder.verifierName = verifier.name;
        return registry.add(newOrder);
    })
    .catch(function (err){
        throw new Error(err);
    });
 }

/**
 * Verify Document
 * @param {org.important.mynetwork.verificationComplete} veriComp  - the verification to be completed
 * @transaction
 */

function completeVerific (veriComp){
    // pay verifier and change verification status of the document
    var docRegistry;
    var bankRegistry;
    var bankID; 
    var verifierRegistry 
    var verifierFinal
    var isRequested = false
    return getParticipantRegistry('org.important.mynetwork.Verifier')
    .then (function(registry){
        verifierRegistry = registry
        return registry.get(veriComp.verifierID)
    })
    .then (function (verifier){
        verifier.tokenBalance += 10.0
        verifierFinal = verifier
        return getAssetRegistry('org.important.mynetwork.ClientDocument')
    })
    .then ( function (registry){
        docRegistry = registry;
        return registry.get(veriComp.documentID)
    })
    .then (function (doc){
        bankID = doc.ownerBank
        if(doc.verificationStatus == "Requested"){
            isRequested = true
        }
        doc.verificationStatus = veriComp.status
        if( isRequested) {return docRegistry.update(doc)}
    })
    .then( function(){
        if( isRequested) {return verifierRegistry.update(verifierFinal)}
    })
    .then(function(){
        
        return getParticipantRegistry('org.important.mynetwork.Bank')
    })
    .then(function(registry){
        bankRegistry = registry
        return registry.get(bankID.getIdentifier())
    })
    .then(function(bank){
        bank.tokenBalance -=10.0
        if(isRequested){return bankRegistry.update(bank)}
    })   
    .catch(function (err){
        throw new Error(err);
    });

 }

 
/**
 * Verify Document
 * @param {org.important.mynetwork.clientAllowsBank} action  - the verification to be completed
 * @transaction
 */

function clientAllowsBankzz (action){
    var bankRegistry
    var ownerBankID
    var isSameBank = false

    return getAssetRegistry('org.important.mynetwork.ClientDocument')
    .then(function(registry){
        return registry.get(action.documentID)
    })
    .then(function(doc){
        ownerBankID = doc.ownerBank.getIdentifier()
        if(ownerBankID == action.bankID){
            isSameBank = true
        }
        return getParticipantRegistry('org.important.mynetwork.Bank')
    })
    .then (function (registry){
        bankRegistry = registry
        return registry.get(action.bankID)
    })
    .then( function (bank) {
        if( ! isSameBank )
        {
            array = bank.docsWatching
            if(array == null || array.length == 0 ){
                array = [action.documentID];
            }
            else if ((array.indexOf(action.documentID) == -1 )){
                array.push(action.documentID);
            }
            bank.docsWatching = array;
            bank.tokenBalance -= 10;

            return bankRegistry.update(bank)
        }
    })
    .then(function(){
        return bankRegistry.get(ownerBankID)
    })
    .then(function(bank){
        if(! isSameBank){
            bank.tokenBalance += 10.0

            return bankRegistry.update(bank)
        }
    });

}













