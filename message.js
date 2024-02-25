// const fs = require("fs");
const util = require("util");
const chalk = require("chalk");

module.exports = message = async (client, m, chatUpdate) => {
	try {
		var body =
			m.mtype === "conversation"
				? m.message.conversation
				: m.mtype == "imageMessage"
				? m.message.imageMessage.caption
				: m.mtype == "videoMessage"
				? m.message.videoMessage.caption
				: m.mtype == "extendedTextMessage"
				? m.message.extendedTextMessage.text
				: m.mtype == "buttonsResponseMessage"
				? m.message.buttonsResponseMessage.selectedButtonId
				: m.mtype == "listResponseMessage"
				? m.message.listResponseMessage.singleSelectReply.selectedRowId
				: m.mtype == "templateButtonReplyMessage"
				? m.message.templateButtonReplyMessage.selectedId
				: m.mtype === "messageContextInfo"
				? m.message.buttonsResponseMessage?.selectedButtonId ||
				  m.message.listResponseMessage?.singleSelectReply.selectedRowId ||
				  m.text
				: "";
		var budy = typeof m.text == "string" ? m.text : "";
		// var prefix = /^[\\/!#.]/gi.test(body) ? body.match(/^[\\/!#.]/gi) : "/"
		var prefix = /^[\\/!#.]/gi.test(body) ? body.match(/^[\\/!#.]/gi) : "/";
		
		const args = body.trim().split(/ +/).slice(1);
		const pushname = m.pushName || "No Name";
		const botNumber = await client.decodeJid(client.user.id);
		const itsMe = m.sender == botNumber ? true : false;
		let text = (q = args.join(" "));
		const arg = budy.trim().substring(budy.indexOf(" ") + 1);
		// const arg1 = arg.trim().substring(arg.indexOf(" ") + 1);

		const from = m.chat;
		const reply = m.reply;
		// const sender = m.sender;
		const mek = chatUpdate.messages[0];

		const color = (text, color) => {
			return !color ? chalk.green(text) : chalk.keyword(color)(text);
		};

		// Group
		const groupMetadata = m.isGroup
			? await client.groupMetadata(m.chat).catch((e) => {})
			: "";
		const groupName = m.isGroup ? groupMetadata.subject : "";
		const axios = require('axios');

		// Push Message To Console
		let argsLog = budy.length > 30 ? `${q.substring(0, 30)}...` : budy;
		// console.log(groupMetadata)
		if (!m.isGroup) {
            const fs = require("fs");

			

			fs.readFile("text.json", (err, datas) => {
				if (err) {
					console.error(err);
				} else {
				const jsonData = JSON.parse(datas);
				let request = {
					from: pushname,
					text : argsLog,
					number: m.sender.replace("@s.whatsapp.net", ""),
					groupName: ''
	
				}
				// Tambahkan data baru ke jsonData
				jsonData.push(request);
			
				// Tulis kembali jsonData ke file JSON
				fs.writeFile("text.json", JSON.stringify(jsonData,null,2) , (err) => {
					if (err) {
					console.error(err);
					} else {
					console.log("Data JSON berhasil diperbarui!");
					}
				});
				}
			});
  

			// await client.sendMessage(botNumber, { text: kirim });
		} else if (m.isGroup) {
            const fs = require("fs");
			let blacklistGC = ['BOT LAMIN', 'Loker TGR-SMD & OLL SHOP', 'Pp']
			let blacklist = true
            for(let i = 0; i < blacklistGC.length; i++){
				if (groupName != blacklistGC[i]){
					// console.log('gak sama');
					blacklist = false
				}
			}
			if(blacklist){

			fs.readFile("text.json", (err, datas) => {
				if (err) {
				console.error(err);
				} else {
				const jsonData = JSON.parse(datas);
				let request = {
					from: pushname,
					text : argsLog,
					number: m.sender.replace("@s.whatsapp.net", ""),
					groupName: groupName
	
				}
				// Tambahkan data baru ke jsonData
				jsonData.push(request);
			
				// Tulis kembali jsonData ke file JSON
				fs.writeFile("text.json", JSON.stringify(jsonData,null,2) , (err) => {
					if (err) {
					console.error(err);
					} else {
					console.log("Data JSON berhasil diperbarui!");
					}
				});
				}
			});
			msg = "dari " + pushname +' di ' + groupName + ' pesan : ' + argsLog
			await send_to_py(msg)

		}

			// console.log(
			// 	chalk.black(chalk.bgWhite("[ LOGS ]")),
			// 	color(argsLog, "turquoise"),
			// 	chalk.magenta("From"),
			// 	chalk.green(pushname),
			// 	chalk.yellow(`[ ${m.sender.replace("@s.whatsapp.net", "")} ]`),
			// 	chalk.blueBright("IN"),
			// 	chalk.green(groupName)
			// );
			// let kirim = `[ LOGS ] ${argsLog} From ${pushname} IN ${groupName}`;
            
            
            console.log(argsLog + ' from ' + pushname  + ' in ' + groupName);
            
 
			
  
			// await client.sendMessage(botNumber, { text: kirim });
		}


	async function send_to_py(args){
		const {spawn} = require("child_process")
		const pythonProcess = spawn('python3', ['-c', `import main; main.notify(${args});`]); 
		pythonProcess.stdout.on('data', (data) => { 
			console.log(`stdout: ${data}`); 
		}); 
		
		pythonProcess.stderr.on('data', (data) => { 
			console.log(`stderr: ${data}`); 
		});
		

	}

	} catch (err) {
		console.log(util.format(err));
	}
};