package net.swordie.ms.connection.packet;

import net.swordie.ms.client.character.Char;
import net.swordie.ms.client.character.commands.AdminCommands;
import net.swordie.ms.connection.OutPacket;
import net.swordie.ms.handlers.header.OutHeader;
import net.swordie.ms.world.shop.NpcShopDlg;
import net.swordie.ms.world.shop.result.ShopResult;

/**
 * Created on 3/28/2018.
 */
public class ShopDlg {

    public static OutPacket openShop(Char chr, int petTemplateID, NpcShopDlg nsd) {
        OutPacket outPacket = new OutPacket(OutHeader.SHOP_OPEN);

        outPacket.encodeInt(nsd.getNpcTemplateID());
        outPacket.encodeByte(petTemplateID != 0);
        if (petTemplateID != 0) {
            outPacket.encodeInt(petTemplateID);
        }
        nsd.encode(outPacket, chr.getBuyBack());
        if (chr.isDebugMode()) {
            chr.chatMessage(AdminCommands.adminChatType, "ShopID: %d", nsd.getNpcTemplateID());
        }

        return outPacket;
    }

    public static OutPacket shopResult(ShopResult shopResult) {
        OutPacket outPacket = new OutPacket(OutHeader.SHOP_RESULT);

        shopResult.encode(outPacket);

        return outPacket;
    }
}
