import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;

import java.io.PrintWriter;

public class DecompileFunction extends GhidraScript {
    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) {
            printerr("Usage: DecompileFunction <hex-addr> <out-file>");
            return;
        }
        long addrLong = Long.parseUnsignedLong(args[0].replaceFirst("^0x", ""), 16);
        Address addr = currentProgram.getAddressFactory().getDefaultAddressSpace().getAddress(addrLong);
        Function fn = getFunctionContaining(addr);
        if (fn == null) fn = getFunctionAt(addr);
        if (fn == null) {
            printerr("No function at 0x" + Long.toHexString(addrLong));
            return;
        }
        println("Decompiling " + fn.getName() + " @ " + fn.getEntryPoint());
        DecompInterface d = new DecompInterface();
        d.openProgram(currentProgram);
        DecompileResults res = d.decompileFunction(fn, 300, monitor);
        if (!res.decompileCompleted()) {
            printerr("Decompile failed: " + res.getErrorMessage());
            return;
        }
        String c = res.getDecompiledFunction().getC();
        try (PrintWriter pw = new PrintWriter(args[1])) {
            pw.println("// Function: " + fn.getName() + " @ 0x" + Long.toHexString(addrLong));
            pw.println(c);
        }
        println("Wrote " + c.length() + " bytes to " + args[1]);
    }
}
