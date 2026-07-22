import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.symbol.Reference;
import ghidra.program.model.symbol.ReferenceIterator;

public class XrefsToAddr extends GhidraScript {
    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 1) { printerr("Usage: XrefsToAddr <hex-addr>"); return; }
        long addrLong = Long.parseUnsignedLong(args[0].replaceFirst("^0x", ""), 16);
        Address addr = currentProgram.getAddressFactory().getDefaultAddressSpace().getAddress(addrLong);
        println("Xrefs to 0x" + Long.toHexString(addrLong) + ":");
        ReferenceIterator it = currentProgram.getReferenceManager().getReferencesTo(addr);
        int count = 0;
        while (it.hasNext()) {
            Reference r = it.next();
            Address from = r.getFromAddress();
            Function fn = getFunctionContaining(from);
            String fnName = (fn == null) ? "?" : fn.getName();
            println("  from " + from + " (" + fnName + ") type=" + r.getReferenceType());
            count++;
            if (count > 200) { println("  ... (truncated)"); break; }
        }
        println("Total: " + count);
    }
}
