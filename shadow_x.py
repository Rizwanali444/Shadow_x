import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode('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'))))
