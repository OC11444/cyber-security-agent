export const idlFactory = ({ IDL }) => {
  return IDL.Service({
    'get_logs' : IDL.Func([], [IDL.Vec(IDL.Text)], ['query']),
    'log' : IDL.Func([IDL.Text], [IDL.Text], []),
  });
};
export const init = ({ IDL }) => { return []; };
