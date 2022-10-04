import subprocess as s
phone = ["9963251442","8547323665","8056783625"]
for x in phone:
  out = s.run(["truecallerjs","-s",x,"--text"],capture_output=True)
  print(out.stdout.decode())