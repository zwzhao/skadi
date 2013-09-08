from skadi import index as i
from skadi.protoc import demo_pb2 as pb_d


def construct(io, tick=0):
  iter_entries = iter(io)

  def advance():
    p, m = next(iter_entries)
    if p.kind == pb_d.DEM_SyncTick:
      raise StopIteration()
    return (p, m)

  return Index(((p, m) for p, m in iter(advance, None)))


class Index(i.Index):
  def __init__(self, iterable):
    super(Index, self).__init__(iterable)

  @property
  def dem_file_header(self):
    return self.find(pb_d.DEM_FileHeader)

  @property
  def dem_class_info(self):
    return self.find(pb_d.DEM_ClassInfo)

  @property
  def dem_send_tables(self):
    return self.find(pb_d.DEM_SendTables)

  @property
  def all_dem_signon_packet(self):
    return self.find_all(pb_d.DEM_SignonPacket)
