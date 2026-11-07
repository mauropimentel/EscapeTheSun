import {mkdir,copyFile,readFile} from 'node:fs/promises';
import {resolve} from 'node:path';
const source=resolve('index.html');
const html=await readFile(source,'utf8');
if(!html.includes('ESCAPE THE SUN')||!html.includes('</html>'))throw new Error('Expected complete game index.html at repository root');
await mkdir(resolve('www'),{recursive:true});
await copyFile(source,resolve('www/index.html'));
console.log('Prepared www/index.html from the existing game without modifying its source.');
