const http = require('http');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const PORT = process.env.PORT || 8000;
const BASE_DIR = __dirname;

const MIME_TYPES = {
    '.html': 'text/html; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.js': 'application/javascript; charset=utf-8',
    '.json': 'application/json; charset=utf-8',
    '.csv': 'text/csv; charset=utf-8',
    '.md': 'text/markdown; charset=utf-8',
    '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.ico': 'image/x-icon',
    '.svg': 'image/svg+xml'
};

const server = http.createServer((req, res) => {
    let safeUrl = decodeURI(req.url.split('?')[0]);
    if (safeUrl === '/' || safeUrl === '') {
        safeUrl = '/index.html';
    }

    const filePath = path.join(BASE_DIR, safeUrl);

    if (!filePath.startsWith(BASE_DIR)) {
        res.writeHead(403, { 'Content-Type': 'text/plain' });
        res.end('403 Forbidden');
        return;
    }

    fs.stat(filePath, (err, stats) => {
        if (err || !stats.isFile()) {
            res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
            res.end(`404 Not Found: ${safeUrl}`);
            return;
        }

        const ext = path.extname(filePath).toLowerCase();
        const contentType = MIME_TYPES[ext] || 'application/octet-stream';

        res.writeHead(200, {
            'Content-Type': contentType,
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        });

        const stream = fs.createReadStream(filePath);
        stream.pipe(res);
    });
});

server.listen(PORT, () => {
    const url = `http://localhost:${PORT}/`;
    console.log('='.repeat(65));
    console.log('  SIPEDBD (Sistem Informasi Prediksi dan Analisis DBD)');
    console.log('='.repeat(65));
    console.log(`[*] Server aktif berjalan di : ${url}`);
    console.log('[*] Tekan CTRL + C di terminal untuk menghentikan server.');
    console.log('='.repeat(65));

    const startCmd = process.platform === 'win32' ? `start ${url}` : `open ${url}`;
    exec(startCmd, () => {});
});
